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
    if (input == "Hello") {
        return "Hello";
    } else if (input == "goodbye") {
        return "Talk to you later!";
    }

    if (input === "@assistenza"){
        return "Turn to cineticket.project@gmail.com";
    }
    else if (input == "@problemilogin") {
        return "You have various possibilities including registering via the form or using google access " +
            "for further problems contact cineticket.project@gmail.com";
    }
     else if (input == "@promozione") {
        return "Before receiving the promotional code to show at the counter, sign up and enter " +
            "to be part of our community";
    }
     if (input == "OK") {
         return "Try asking for more!";
     }

}