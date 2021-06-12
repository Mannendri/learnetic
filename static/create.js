const addFlashcardButton = document.querySelector(".button");
const form = document.querySelector("form");


addFlashcardButton.addEventListener("click",addFlashcard);

function addFlashcard(e){
    e.preventDefault();
    document.querySelector("div.flash:last-of-type").after(createFlashcard());
    
}

function createFlashcard(){
    let lastFlashcard = document.querySelector("div.flash:last-of-type");
    return lastFlashcard.cloneNode(true);
}
