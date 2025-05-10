import sys

def parse_dimacs(filename):
    formula = []
    with open(filename, 'r') as file:
        for line in file:
            if line.startswith('c') or line.startswith('p'):
                continue
            literals = list(map(int, line.strip().split()))
            if literals[-1] == 0:
                literals = literals[:-1]
            formula.append(set(literals))
    return formula

def resolvable(cl1, cl2):
    for lit in cl1:
        if -lit in cl2:
            new_clause = (cl1 - {lit}) | (cl2 - {-lit})
            return True, new_clause
    return False, None

def resolution(formula):
    formula = [frozenset(c) for c in formula]
    new = set()

    while True:
        n = len(formula)
        for i in range(n):
            for j in range(i + 1, n):
                resolvable_flag, resolvent = resolvable(formula[i], formula[j])
                if resolvable_flag:
                    if not resolvent:
                        return "UNSAT"
                    new.add(frozenset(resolvent))

        if new.issubset(set(formula)):
            return "SAT"
        for c in new:
            if c not in formula:
                formula.append(c)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Utilizare: python rezolutie.py <fisier_dimacs>")
        sys.exit(1)

    filename = sys.argv[1]
    formula = parse_dimacs(filename)
    result = resolution(formula)
    print(result)