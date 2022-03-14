const productos = [
  {
    id:1
  },
  {
    id:2
  },
  {
    id:3
  }
];

function getproducts(){
  return new Promise((resolve, reject) => {
    setTimeout(()=>{
      resolve(productos);
    }, 3000);
  })
}


async function gp(){
  let mp = await getproducts();
  console.log(mp);
}

function pr(e){
  return new Promise((res,rej) => {
    setTimeout(()=>{
      res(e);
    },1000)
  })
}

async function be(){
  for (let i = 0; i < 10; i++) {
    let x = await pr(i);
    console.log(x);
  }
}

be();


