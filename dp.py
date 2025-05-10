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
            formula.append(set(literals))
    return formula

def get_variables(formula):
    return set(abs(lit) for clause in formula for lit in clause)

def resolve(c1, c2, var):
    if var in c1 and -var in c2:
        return (c1 - {var}) | (c2 - {-var})
    elif -var in c1 and var in c2:
        return (c1 - {-var}) | (c2 - {var})
    return None

def dp(formula):
    while True:
        if not formula:
            return "SAT"
        if set() in formula:
            return "UNSAT"

        variables = get_variables(formula)
        if not variables:
            return "SAT"

        var = variables.pop()
        pos_clauses = [c for c in formula if var in c]
        neg_clauses = [c for c in formula if -var in c]

        new_clauses = []
        for c1 in pos_clauses:
            for c2 in neg_clauses:
                resolvent = resolve(c1, c2, var)
                if resolvent is None:
                    continue
                if not resolvent:
                    return "UNSAT"
                new_clauses.append(resolvent)

        old_len = len(formula)
        formula = [c for c in formula if var not in c and -var not in c]
        formula.extend(new_clauses)

        if len(formula) == old_len:
            return "SAT"

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Utilizare: python dp.py <fisier_dimacs>")
        sys.exit(1)

    filename = sys.argv[1]
    formula = parse_dimacs(filename)
    result = dp(formula)
    print(result)