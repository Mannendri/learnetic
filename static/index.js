let sets = document.getElementsByClassName("set");

for(i=0;i<sets.length;i++){
    sets[i].addEventListener("click",goToStudy);
}

function goToStudy(e){
    let set = e.currentTarget;
    let setName = set.querySelector('h2').innerHTML;
    let setDescription = set.querySelector('h3').innerHTML;
    console.log(setName);
    console.log(setDescription);

    let xhr = new XMLHttpRequest();
    xhr.open("POST", '/study', true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.send(JSON.stringify({
        "values": {"name":setName,
                   "description":setDescription
                }
    }));
    // window.location="/study";
}