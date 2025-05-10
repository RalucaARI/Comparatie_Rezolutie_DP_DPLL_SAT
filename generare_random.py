import random

def generate_random_cnf(num_vars, num_clauses, clause_len_range=(2, 3)):
    cnf = []
    for _ in range(num_clauses):
        clause_len = random.randint(*clause_len_range)
        clause = set()
        while len(clause) < clause_len:
            var = random.randint(1, num_vars)
            lit = var if random.choice([True, False]) else -var
            clause.add(lit)
        cnf.append(list(clause))
    return cnf

# Generăm un exemplu cu 5 variabile și 4 clauze
example_cnf = generate_random_cnf(num_vars=5, num_clauses=4)

# Pregătim în format DIMACS
dimacs_lines = ["c exemplu generat automat", f"p cnf 5 4"]
for clause in example_cnf:
    dimacs_lines.append(" ".join(map(str, clause)) + " 0")

dimacs_output = "\n".join(dimacs_lines)
print(dimacs_output)