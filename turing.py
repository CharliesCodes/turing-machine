
# =============================================================================
# Created By  : Dominique Zeise
# GitHub      : https://github.com/CharliesCodes
# Created Date: 2021/11/11
# Version     : 1.0
# © Copyright : 2021 Dominique Zeise
# =============================================================================
'''The Module is a Turing machine with excel spreadsheets for instructions'''
# =============================================================================


def main():
    import pandas as pd

    # Enter spreadsheet name E.g. "Multiplication", "Invert" or "Addition"
    instructions = "Invert"
    df = pd.read_excel('instructions.xlsx', header=0,
                    sheet_name=instructions).astype("string")

    tape = list("#11101#")
    run_machine(df, tape)


def run_machine(df, tape):
    index, state, run = 0, 0, True
    while run:
        symbol = tape[index]
        current_row = df.loc[
            (df.State == str(state)) & (df.Symbol == str(symbol))]
        state = current_row.State_new.values[0]
        tape[index] = current_row.Symbol_new.values[0]
        move = current_row.Move.values[0]
        if move == "r":
            index += 1
        elif move == "l":
            index -= 1
        elif move == "stop" or state == "error":
            run = False
            break
    print(f"End State reached.\nResult: {''.join(tape)}")


if __name__ == '__main__':
    main()
