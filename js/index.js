function step1(item,nextstep){
  alert('you have ordered item ${item}')
  setTimeout(()=>{
    nextstep()
  },2000)
}
step1("laptop dell",()=>{
  alert("your laptop dell order shipped succesfully!!!")
})

-