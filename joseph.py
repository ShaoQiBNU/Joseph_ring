def joseph(n,q):
    if n==1:
        return 0
    else:
        return (joseph(n-1,q)+q)%n


if __name__ == '__main__':
    n=1
    q=3
    res=joseph(n,q)+1
    print(res)
