def String(n):
    strg = ""
    for i in range(n):
        strg += f"{i+1}"
    return strg

if __name__ == '__main__':
    n = int(input())
    print(String(n))