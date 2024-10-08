if __name__ == "__main__":
    for _ in range(int(input())):
        a, b = list(map(int, input().strip().split()))
        if a%2 != 0:
            print("NO")
        else:
            if b%2 == 0:
                print("YES")
            else:
                if a >= 2:
                    print("YES")
                else:
                    print("NO")
