def levenshtein(s1, s2):
    d = {}
    lenstr1 = len(s1)
    lenstr2 = len(s2)
    for i in range(-1,lenstr1+1):
        d[(i,-1)] = i+1
    for j in range(-1,lenstr2+1):
        d[(-1,j)] = j+1

    for i in range(lenstr1):
        for j in range(lenstr2):
            if s1[i] == s2[j]:
                cost = 0
            else:
                cost = 1
            d[(i,j)] = min(
                           d[(i-1,j)] + 1, # deletion
                           d[(i,j-1)] + 1, # insertion
                           d[(i-1,j-1)] + cost, # substitution
                          )
            if i and j and s1[i]==s2[j-1] and s1[i-1] == s2[j]:
                d[(i,j)] = min (d[(i,j)], d[i-2,j-2] + cost) # transposition
    return d[lenstr1-1,lenstr2-1]


def make_correction(users_str, correct_str, starc_mark, end_mark):
    start_of_str = ''
    end_of_str = ''
    #go through the stirng from begin and find the point of discrepancy
    for c in range(len(correct_str)):
        if users_str[c] != correct_str[c]:
            #when the discrepancy detected, we slice the begin of the string in this point 
            start_of_str = correct_str[:c]
            break
        if len(users_str)-1==c:
            #when this is True: means that mistake in the last symbol
            #we need slicte unlit this point
            start_of_str = correct_str[:c+1]
            break
    else:
        #this will be when users's stirng contains additional symbol in the end, but the begin in correct
        start_of_str = correct_str

    #go through the string from end and do the same
    for c in range(len(correct_str)):
        #index from end
        i = -c-1
        if users_str[i] == correct_str[i]:
            end_of_str = correct_str[i] + end_of_str
            if len(users_str)==-i:
                #when users's sting is over -we should brake this cycle
                break
        else:
            break
    
    if start_of_str+end_of_str == correct_str:
        #will be True when extra syblol added in the user's string and we should underline two symbols
        if start_of_str != '':
            start_of_str = start_of_str[:-1]+starc_mark+start_of_str[-1]
        else:
            start_of_str = starc_mark
        
        if end_of_str != '':
            end_of_str = end_of_str[0]+end_mark+end_of_str[1:]
        else:
            end_of_str = end_mark
    else:
        begin_str_len = len(start_of_str)
        end_str_len = len(end_of_str)

        #the next string after discrepancy point must be underlined, it is typo
        if (start_of_str!=''):
            start_of_str += starc_mark+correct_str[begin_str_len]
        else:
            start_of_str = starc_mark+correct_str[begin_str_len]

        if (begin_str_len+end_str_len+1==len(correct_str)):
            #when one symbol is incorrect
            end_of_str = end_mark+end_of_str
        else:
            #when two symnols are swapped
            end_of_str = correct_str[begin_str_len+1]+end_mark+end_of_str
    return(start_of_str+end_of_str)


def check_answer(users_str, correct_str, starc_mark, end_mark):
    index = levenshtein(users_str, correct_str)
    if index > 1:
        return 0
    elif index == 0:
        return 1
    else:
        return make_correction(users_str, correct_str, starc_mark, end_mark)
