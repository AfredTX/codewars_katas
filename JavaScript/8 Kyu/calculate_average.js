/*
Write a function which calculates the average of the numbers in a given list.

Note: Empty arrays should return 0.

 */

function findAverage(array) {
  if (array.length > 0) {
    const average = array => array.reduce((a,b) => a + b)/array.length;
    return average(array);
  }
  return 0;
}