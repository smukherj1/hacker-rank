import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {
    
    private static void find_pmax(int[] num_array)
    {
        long best_sum = 0;
        for(int i = 0; i < num_array.length; ++i)
        {
            long cur_sum = num_array[i];
            int idx = 2;
            int j;
            if(i == (num_array.length - 1))
            {
                j = 0;
            }
            else
            {
                j = i + 1;
            }
            for(; (j != i); j = ((j + 1) % num_array.length), idx++)
            {
                cur_sum += idx * num_array[j];
            }
            if(cur_sum > best_sum)
            {
                best_sum = cur_sum;
            }
        }
        System.out.println(best_sum);
    }

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        try 
        {
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
 
		    String num_integers = br.readLine();
            String num_array_str = br.readLine();
            String []num_str_array = num_array_str.split(" ");
            int []num_arr = new int[num_str_array.length];
            int i = 0;
            for(String num_str : num_str_array)
            {
                num_arr[i++] = Integer.parseInt(num_str);
            }
            find_pmax(num_arr);
	     } 
        catch(IOException io) 
        {
            io.printStackTrace();
	    }	
    }
}