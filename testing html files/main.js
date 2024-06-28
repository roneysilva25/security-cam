function handlerIn() {
    $(".disappear").fadeIn();
    setTimeout(() => {
        $(".disappear").fadeOut();
    }, 10000);
}

function giveFeedback (texto) {
    $(".feedback").text(texto)
    $(".feedback").css("visibility", "visible")
    setTimeout(() => {
        $(".feedback").css("visibility", "hidden")
    }, 5000)
}

function gotClicked() {
    let id = this.id;
    switch (id) {
        case "picture":
            giveFeedback("Tirando foto...Será enviada ao Telegram.")
            break;
        case "record":
           giveFeedback("Gravando vídeo de 30 segundos...Será enviado ao Telegram.")
            break
        case "detect":
           giveFeedback("Detector de pessoas.")
            break
    }
}


$(".div1").on( "mouseenter click load", handlerIn);

var setLenght = document.querySelectorAll(".withFeedback").length;
for (var i = 0; i < setLenght; i++) {
    document.querySelectorAll(".withFeedback")[i].addEventListener("click", gotClicked);
}