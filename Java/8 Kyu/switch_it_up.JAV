/*
When provided with a number between 0-9, return it in words.

Input :: 1

Output :: "One".
*/

public class Kata
{
  public static String switchItUp(int number)
  {
    String[] arr = {"Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"};
    return arr[number];
  }
}