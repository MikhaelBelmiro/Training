import sys

def insertion_sort(x:list, method:str):
    available_method = ['increasing', 'decreasing']
    if method not in available_method:
        raise ValueError('method argument should be on of [\'increasing\', \'decreasing\'')
    
    if method == 'increasing':
        for j in range(1, len(x)):
            temp = x[j]
            i = j-1
            while i>-1 and x[i]>temp:
                x[i+1] = x[i]
                i -= 1
            x[i+1] = temp
            print('The order of the list is now',x)
        return f'The ordered list is {x}'

    if method == 'decreasing':
        for j in range(1, len(x)):
            temp = x[j]
            i = j-1
            while i>-1 and x[i]<temp:
                x[i+1] = x[i]
                i -= 1
            x[i+1] = temp
            print('The order of the list is', x)
        return f'The ordered list is{x}'

if __name__ == '__main__':
    method = sys.argv[1]
    sys_input = [int(x) for x in sys.argv[2:]]
    print('Sorted list is',insertion_sort(sys_input, method))