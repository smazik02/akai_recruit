<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <title>Arrays</title>
</head>

<body>
    <form action="" method="POST">
        <p>Input a sentence <input type="text" name="a"></p>
        <input type="submit" value="Send" name="send">
    </form>
    <?php
    if (isset($_POST['send'])) {
        @$sentence = $_POST['a'];
        $words = explode(" ", $sentence);
        print_r($words); echo "<br>";
        $count=count($words);
        for ($i = 0; $i < $count; $i++) {
            if (strlen($words[$i]) < 4) {
                unset($words[$i]);
            }
        }
        print_r($words);
    }
    ?>
</body>

</html>