/*
Write a function that returns a string in which firstname is swapped with last name.

Example(Input --> Output)

"john McClane" --> "McClane john"

 */

function nameShuffler(str){
  const name = str.split(" ");
  return [name[1], name[0]].join(" ");
}