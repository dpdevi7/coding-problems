

## EXCELLENT DEVI !!!
## NICE JOB


def convertFive(number):

    ## read all elements for loop
    ## if a element=0 --> convert it to 5
    ## failed cases = 000=555, 001=551

    decimalPlace = 1
    new_num = 0

    while number > 0:

        percentile = number%10

        if percentile == 0:
            percentile = 5

        multiply_percentile = percentile * decimalPlace
        new_num = new_num + multiply_percentile

        number = number // 10
        decimalPlace = decimalPlace * 10

    return new_num


def recursive_function(original_num, length, count, percentile, division, decimal, ans):

    if length == count:
        return ans
    else:
        if (percentile == 0):
            percentile = 5

        ans = percentile * decimal + ans
        count = count + 1




        return recursive_function(original_num=original_num,
                                  length=length,
                                  count=count,
                                  percentile=division%10,
                                  division=division//10,
                                  decimal=decimal*10,
                                  ans=ans)


    pass


def recursive_convert_5(number_str):
    number = int(number_str)

    ## solution for every cases --> 000=555, 001=551, 1001=1551

    ## python taking int input of multiple zeros as single 0, e.g --> input = 000, python will take 0.
    ## so the length of input will always 1.
    ## solution: taking input as string
    ## recursive approach
    ## idea: takeing length as solution. if counter==length: return answer

    ## taking number as a string.

    return recursive_function(original_num=number,
                              length=len(number_str),
                              count=0,
                              percentile=number%10,
                              division=number//10,
                              decimal=1,
                              ans=0)



if __name__ == '__main__':

    ## given number 1005 --> 1555 (replace 0 with 5)
    t = int(input("test cases: "))

    for i in range(t):
        print(recursive_convert_5(input("enter number: ").strip()))



