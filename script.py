def readInput(filePath: str):
    lines = []
    with open(f"{filePath}", 'r') as f:
        lines = f.readlines()

    return lines