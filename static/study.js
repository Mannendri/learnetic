// function answerFunction() {
//     /*After clicking the button, I want to set the default value.
//     Is that something we can do or can we just do: = {{ ... }}*/
//     document.getElementById("answer").innerHTML = "default value";
// }

let flashcards = document.getElementsByClassName("flashcard");
let check = true;

for(i=0;i<flashcards.length;i++){
    flashcard = flashcards[i]
    flashcard.addEventListener("click",toggleFlashcard);
    flashcard.querySelector(".definition").style.display="none";
}
function toggleFlashcard(e){
    check=!check;
    let flashcard = e.currentTarget;
    if (check==true){
        let term = flashcard.querySelector(".term");
        term.style.display="block";
        let definition = flashcard.querySelector(".definition");
        definition.style.display="none";

    }
    else {
        let term = flashcard.querySelector(".term");
        term.style.display="none";
        let definition = flashcard.querySelector(".definition");
        definition.style.display="block";
    }
}