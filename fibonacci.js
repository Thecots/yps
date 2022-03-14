console.clear();

function main(e){
  let l = 0;
  for(let i = 0; i <= 10; i++){
    console.log(`${l}+${i}=${l+i}`);
    l = l + i
  }
  return l
}


console.log(main(10));

