def find_sum_array(list_input,sum_of_numbers,length_of_list):
    list_input.sort()
    for i in range(0,length_of_list):
        # proceed only if the number is less than sum
        if list_input[i]<sum_of_numbers:
            difference = sum_of_numbers-list_input[i]
            # check whether the diff is available in the list
            for j in range(i,length_of_list):
                # if number is equal to difference then it will add up to sum provided, hence return true 
                if list_input[j] == difference:
                    return "Yes"
                    break
                # if number is greater than difference then rest of numbers will not add up to sum provided, hence break loop
                elif list_input[j] > difference:
                    break
        else:
            return "No"
    return "No"

T = int(input())
for t_cases in range(0,T):
    N,X = input().split()
    input_list = list(map(int, input().split()))
    print(find_sum_array(input_list,int(X),int(N)))
