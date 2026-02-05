console.log("abc")
let demo=document.getElementById("demo"),
mobile=document.getElementById("mobile"),
h1=document.getElementById("h1-1"),
ptag1=document.getElementById("p-tag1"),
pic1=document.getElementById("img-1")

img=false



demo.addEventListener("click",function(){
    // img=1
    
    
    if(img==true){
            

             mobile.src="../images/hero_endframe__cvklg0xk3w6e_large 2 (1).png"
            h1.innerText="Upto 10% of voucher"
            h1.style.textAlign="center"
            ptag1.innerText="iphone 16 series"
            pic1.src="../images/1200px-Apple_gray_logo 1.png"
            
            }
    else{
        mobile.src="../images/Card1.png"
            h1.innerText="Upto 25% of voucher"
            h1.style.textAlign="center"
            ptag1.innerText="New fashion hear"
            pic1.src="../images/nike1.jpeg"
            pic1.style="height:50px;width:50px;border-radius:50%;"
           
          
    }
    img=!img
 
})


let days=document.getElementById("days"),
hours=document.getElementById("hours"),
min=document.getElementById("minutes"),
sec=document.getElementById("seconds"),
sdays=3,
shours=15,
sminutes=45,
sseconds=20;






    let coundown=setInterval( ()=>{
           sseconds--;
           if(sseconds<0){
            sseconds=59
            sminutes--
           }

           if(sminutes<0){
                sminutes=59
                shours--
           }

           if(shours<0){
                shours=23
                sdays--
           }

           if(sdays<0){
                sdays=shours=sminutes=sseconds=0;
           }

           days.innerText=sdays<10 ? "0"+sdays : sdays
           hours.innerText=shours<10 ? "0"+shours : shours
           min.innerText=sminutes<10 ? "0"+sminutes : sminutes
           sec.innerText=sseconds<10 ? "0"+sseconds : sseconds
    },1000)



    function cart(){
     let carticon=document.querySelector('[data-cart-url]');
     let url=carticon.getAttribute('data-cart-url')
     window.location.href=url;
    }

    function whistle(){
      let carticon=document.querySelector('[data-whistle-url]');
     let url=carticon.getAttribute('data-whistle-url')
     window.location.href=url;

     
    }

    let serch=document.getElementById('ser')
    let focuses=document.getElementById('foc')

    serch.addEventListener(("click"),()=>{
               focuses.focus()
    })

    


    



   