<?php

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $username = $_POST["username"];
    $password = $_POST["password"];

    if (empty($username) || empty($password)) {
        echo "Veuillez remplir tous les champs.";
    }else {
        $servername = "localhost";
        $db_username = "votre_identifiant";
        $db_password = "votre_mot_de_passe";
    }
}

