async function init(){
  div = document.querySelector('div#row1');
  for(let i = 0; i < div.childElementCount-1; i++){
      let x = await printWord(div.children[i].innerText);
      document.querySelector('div#input-row input').value = x;
  }
}

function printWord(e){
  return new Promise((res,rej) => {
      setTimeout(() => {
          res(e);
      },001)
  })
}

setTimeout(()=>{
  init()
},4000)