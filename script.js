const mainBox = document.querySelector(".box");

const plySelectedOpt = document.querySelector(".selection");

const cmpSelection = document.querySelector(".cmpSelection");

const playerOptResult = document.querySelector(".plySelection");

const finalResult = document.querySelector(".gameChanger");
const cmp = document.querySelector(".computerOpt");
const scorePly = document.querySelector(".plyScore");
const cmpScore = document.querySelector(".cmpScore");

const playerOpt = document.querySelector(".playerOpt");

const data = ["Rock","Paper","Scissor"];

const computer = document.querySelector(".computer");
const player = document.querySelector(".player");
const images = document.querySelectorAll(".images");



function handleClick(event){
  const player = (event.target.dataset.opt);
  //player.innerHTML = `${choose.innerHTML}`;

  const cmpRandom = data [Math.floor(Math.random() * data.length)];
  
        //Generate Random Number For Computer turn
       //if (cmpRandom === 0) {
         //   computer.innerHTML = `<i class="fas fa-hand-rock"></i>`;
       // } else if (cmpRandom === 1) {
           // computer.innerHTML = `<i class="fas fa-hand-paper"></i>`;
        //} else if (cmpRandom === 2) {
            //computer.innerHTML = `<i class="fas fa-hand-scissors"></i>`;
        //}
      playerOptResult.innerText = player;
      cmpSelection.innerText = cmpRandom;
      cmp.style.color = "blue";
      playerOpt.style.color = "white";
      finalResult.style.padding = "10px";
      if(player == cmpRandom){
      finalResult.innerText = "It's a tie"
      cmp.style.color = "violet";
      playerOpt.style.color = "violet";
      }else if( player == "Rock"){
      if(cmpRandom == "Paper"){
        cmpScore.innerText = Number(cmpScore.innerText) + 1;
        playerOpt.style.color = "red";
        cmp.style.color = "green";
          return finalResult.innerText = "You Lose! Don't demotivate play again.";
          
         
      }else{
          scorePly.innerText = Number(scorePly.innerText) + 1;
          playerOpt.style.color = "Green";
          cmp.style.color = "red";
          return finalResult.innerText = "You Won! Congrats."
          
      }
      }else if(player == "Paper"){
      if(cmpRandom == "Rock"){
        scorePly.innerText = Number(scorePly.innerText) + 1;
        playerOpt.style.color = "Green";
        cmp.style.color = "red";
          return finalResult.innerText = "You Won! Congrats."
          
      }else{
        cmpScore.innerText = Number(cmpScore.innerText) + 1;
        playerOpt.style.color = "red";
        cmp.style.color = "green";
          return finalResult.innerText = "You Lose! Don't demotivate,play again."
      }
      }else if( player == "Scissor"){
      if(cmpRandom == "Paper"){
        scorePly.innerText = Number(scorePly.innerText) + 1;
        playerOpt.style.color = "Green";
        cmp.style.color = "red";
          return finalResult.innerText = "You Won! Congrats."
      }else
      cmpScore.innerText = Number(cmpScore.innerText) + 1;
      playerOpt.style.color = "red";
      cmp.style.color = "green";
        return finalResult.innerText = "You Lose! Don't demotivate Play again."
  }
}


playerOpt.addEventListener("click",handleClick);
  




 





