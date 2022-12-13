function getBotResponse(input) {
    //rock paper scissors
    if (input == "rock") {
        return "paper";
    } else if (input == "paper") {
        return "scissors";
    } else if (input == "scissors") {
        return "rock";
    }

    // Simple responses
    if (input == "ciao") {
        return "ciao";
    } else if (input == "goodbye") {
        return "Talk to you later!";
    }

    if (input === "@assistenza"){
        return "rivolgersi a cineticket.project@gmail.com";
    }
    else if (input == "@problemilogin") {
        return "Hai varie possibilità tra cui iscriverti tramite il form oppure usare l'accesso di google " +
            "per ulteriori problemi contattare cineticket.project@gmail.com";
    }
     else if (input == "@promozione") {
        return "Prima di ricevere il codice promozionale da mostrare allo sportello, iscriviti ed entra " +
            "a fare parte della nostra community";
    }
    else {
        return "Prova a chiedere altro!";
    }
}