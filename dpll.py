import sys

def parse_dimacs(filename):
    formula = []
    with open(filename, 'r') as file:
        for line in file:
            if line.startswith('c') or line.startswith('p'):
                continue
            literals = list(map(int, line.strip().split()))
            if literals and literals[-1] == 0:
                literals = literals[:-1]
            if literals:
                formula.append(set(literals))
    return formula

def get_literals(formula):
    return set(abs(lit) for clause in formula for lit in clause)

def unit_propagate(formula, assignment):
    changed = True
    while changed:
        changed = False
        unit_clauses = [c for c in formula if len(c) == 1]
        for clause in unit_clauses:
            unit = next(iter(clause))
            assignment.append(unit)
            formula = simplify(formula, unit)
            changed = True
    return formula, assignment

def simplify(formula, literal):
    new_formula = []
    for clause in formula:
        if literal in clause:
            continue
        new_clause = clause - {-literal}
        if not new_clause and -literal in clause:
            return [set()]  # conflict
        new_formula.append(new_clause)
    return new_formula

def dpll(formula, assignment=[]):
    formula, assignment = unit_propagate(formula, assignment)
    if not formula:
        return True
    if set() in formula:
        return False
    lit = next(iter(next(iter(formula))))
    return dpll(simplify(formula, lit), assignment + [lit]) or dpll(simplify(formula, -lit), assignment + [-lit])

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Utilizare: python dpll.py <fisier_dimacs>")
        sys.exit(1)

    filename = sys.argv[1]
    formula = parse_dimacs(filename)
    result = dpll(formula)
    print("SAT" if result else "UNSAT")