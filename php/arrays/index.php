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
    // @author: Marcin Sylka <realmozzar@gmail.com>
    // @date: 28.09.2021
    // @last update: 28.09.2021
    // This is a simple task, which does not require Composer
    // The script will be outputting to a web browser
    // Write a PHP script which will separate every word to key in array
    // example string $str = "Lorem Ipsum is simply dummy text of the printing and typesetting industry."
    // example output: Array ( [0] => Lorem [1] => Ipsum [2] => is [3] => simply [4] => dummy [5] => text [6] => of [7] => the [8] => printing [9] => and [10] => typesetting [11] => industry. )
    // count letters in every word and remove words smaller than 4 letters
    // example output: Array ( [0] => Lorem [1] => Ipsum [3] => simply [4] => dummy [5] => text [8] => printing [10] => typesetting [11] => industry. )
    //
    // Full final output of script:
    // Array ( [0] => Lorem [1] => Ipsum [2] => is [3] => simply [4] => dummy [5] => text [6] => of [7] => the [8] => printing [9] => and [10] => typesetting [11] => industry. )
    // Array ( [0] => Lorem [1] => Ipsum [3] => simply [4] => dummy [5] => text [8] => printing [10] => typesetting [11] => industry. )
    ?>
</body>

</html>