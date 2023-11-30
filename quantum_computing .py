def function_generator(equation,n,m):
    prior = {'^':3, '*':2,'+':1,'-':1}
    lst = []
    mod = 2**m-1
    output={}

    for i in range(len(equation)):
        if equation[i].isdigit():
            lst.append(int(equation[i]))
        else:
            lst.append(equation[i])

    for N in range(2**n):
        result_lst = lst.copy()
        ans = 0
        for s in range(len(result_lst)):
            if result_lst[s] == 'x':
                result_lst[s] = N
        new_eq =''
        for k in range(len(result_lst)):
            if isinstance(result_lst[k],int):
                result_lst[k] = str(result_lst[k])
            new_eq += result_lst[k]
        ans = eval(new_eq)
        ans = ans % mod
        output[N]= ans

    #후위 표기법
    lst2=[]
    for i in range(len(lst)):
        if (i+1)!=len(lst) and lst[i]==lst[i+1] and lst[i] == '*':
            lst2.append('^')
        elif lst[i]==lst[i-1] and lst[i] == '*':
            pass
        else:
            lst2.append(lst[i])

    for t in range(len(lst)):    # 입력받기
        tokens = lst2.copy()
        lst =[]        
        stack = []  # 스택 생성
        for n in range(len(tokens)):    # 토큰의 길이만큼 반복하여
            if str(tokens[n]).isdigit(): # 만약 숫자이면 바로 lst에 추가
                lst.append(tokens[n])
            elif tokens[n] == 'x':
                lst.append(tokens[n])
            else:   # 그외에 경우 tokens[n]이 stack[-1]의 우선순위와 같거나 보다 작으면 tokens[n]의 우선순위가 더 커질때까지 pop
                while stack and prior[tokens[n]] <= prior[stack[-1]]:
                    lst.append(stack.pop()) # pop한것들은 lst에 추가 시켜줌   
                stack.append(tokens[n]) # 위의 조건이 완료 되면 stack에 추가

        while len(stack) != 0:  # stack에 남아있는 연산자들 lst에 추가
            lst.append(stack.pop())
    return output, lst


eq = '3*x**3-4*x+7'
print(function_generator(eq,2,3))