/*
Given two integers a and b, which can be positive or negative, find the sum of all the integers between and including them and return it. If the two numbers are equal return a or b.

Note: a and b are not ordered!
*/

  {
     public int GetSum(int a, int b) {
       int r = 0;

       if (a == b) {
         r = r + a;
       }
       else if (a < b) {
         for (int i = a; i <= b; i++) {
           r = r + i;
         }}
         else {
           for (int i = b; i <= a; i++) {
           r = r + i;
         }
       }return r;
     }
  }