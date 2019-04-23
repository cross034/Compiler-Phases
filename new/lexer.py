import re
from pprint import pprint


def tokenize(code):
    sym_table = {}

    id_matches = re.findall("[a-zA-Z_][a-zA-Z0-9_]*", code)
    lit_matches = re.findall("([0-9]+.[0-9]+|[0-9]+)", code)
    op_matches = re.findall("[=+*/-]", code)

    for id in id_matches:
        sym_table[id] = (len(sym_table), "ID", id)
    for lit in lit_matches:
        sym_table[lit] = (len(sym_table), "LT", lit)

    tokens = []

    start_ptr = 0
    end_ptr = 0
    id_ptr = 0
    lit_ptr = 0
    op_ptr = 0

    while True:
        matched = False
        sub = code[start_ptr:end_ptr]
        if id_ptr < len(id_matches):
            if sub == id_matches[id_ptr]:
                id_ptr += 1
                matched = True
                # print("id token:", sub)
                tokens.append(["ID", sym_table[sub][0]])
        if lit_ptr < len(lit_matches):
            if sub == lit_matches[lit_ptr]:
                matched = True
                lit_ptr += 1
                # print("lit token:", sub)
                tokens.append(["LT", sym_table[sub][0]])
        if op_ptr < len(op_matches):
            if sub == op_matches[op_ptr]:
                matched = True
                op_ptr += 1
                # print("op token:", sub)
                tokens.append([sub])
        if matched:
            start_ptr = end_ptr
        end_ptr += 1
        if end_ptr > len(code):
            break
    return tokens, sym_table


def format_tokens(tokens):
    tokens_formatted = []
    for token in tokens:
        formatted = "<" + str(token)[1:-1] + ">"
        formatted = formatted.replace("'", "")
        tokens_formatted.append(formatted)
    return tokens_formatted
