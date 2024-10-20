s_list = []
def mutate_string(string, position, character):
    for i in string:
        s_list.append(i)
    s_list[position] = character
    s_new = ''.join(s_list)
    return s_new

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)