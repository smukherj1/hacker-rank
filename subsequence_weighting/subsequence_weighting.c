#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

#define BUFSIZE 4096 * 4096
char buf[BUFSIZE];

char* get_next_int(char *str, size_t *result)
{
    *result = 0;
    if(!str)
    {
        return str;
    }
    while(str[0] < '0' || str[0] > '9')
    {
        if(!*str)
        {
            break;
        }
        str++;
    }
    while(str[0] >= '0' && str[0] <= '9')
    {
        size_t val = *result;
        val = (val * 10) + (int)(str[0] - '0');
        *result = val;
        str++;
    }
    return str;
}

void fill_num_arr(char *str, size_t *num_arr, int num)
{
    int i;
    for(i = 0; i < num; ++i)
    {
        size_t next_num;
        str = get_next_int(str, &next_num);
        num_arr[i] = next_num;
    }
}

void handle_test_case()
{
    size_t num;
    size_t *num_arr = NULL, *wt_arr = NULL, *result_wt_arr = NULL;
    // get size of array
    fgets(buf, sizeof(buf), stdin);
    get_next_int(buf, &num);
    num_arr = (size_t*)malloc(num * sizeof(size_t));
    wt_arr = (size_t*)malloc(num * sizeof(size_t));
    result_wt_arr =(size_t*)malloc(num * sizeof(size_t));
    
    fgets(buf, sizeof(buf), stdin);
    fill_num_arr(buf, num_arr, num);
    fgets(buf, sizeof(buf), stdin);
    fill_num_arr(buf, wt_arr, num);
    
    int i, j;
    size_t max = 0;
    for(i = 0; i < num; ++i)
    {
        //printf("(%zu,  %zu)\n", num_arr[i], wt_arr[i]);
        result_wt_arr[i] = wt_arr[i];
        for(j = 0; j < i; ++j)
        {
            if(
                (num_arr[i] > num_arr[j]) && 
                 ((result_wt_arr[j] + wt_arr[i]) > result_wt_arr[i])
              )
            {
                result_wt_arr[i] = result_wt_arr[j] + wt_arr[i];
                if (result_wt_arr[i] > max)
                {
                    max = result_wt_arr[i];
                }
            }
        }
    }
    
    printf("%zu\n", max);
    free(num_arr);
    free(wt_arr);
    free(result_wt_arr);
    return;    
}

int main() {

    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    fgets(buf, sizeof(buf), stdin);
    size_t num_test_cases;
    get_next_int(buf, &num_test_cases);
    while(num_test_cases > 0)
    {
        handle_test_case();
        --num_test_cases;
    }
    return 0;
}