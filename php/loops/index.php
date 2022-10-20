<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <title>Loops</title>
</head>

<body>
    <?php
    $end = "";
    for ($x = 100; $x >= 0; $x--) {
        $num = "";
        if ($x == 0) {
            $num = 0;
        } else {
            if ($x % 4 == 0) {
                $num = "Fire <br>";
            } else if ($x % 7 == 0) {
                $num = "Boom <br>";
            } else {
                $num = "$x <br>";
            }
            if ($x % 10 == 0) {
                $num = '<span style="color:red">' . $num . '</span>';
                $num = str_repeat($num, 10);
            }
        }
        $end .= $num;
    }
    echo "$end";
    // @author: Marcin Lawniczak <marcin@lawniczak.me>
    // @date: 24.10.2017
    // @update: 26.09.2019
    // This is a simple task, which does not require Composer
    // The script will be outputting to a web browser, so use HTML for formatting
    // Write out numbers from 100 to 0, each in a separate line
    // If the number is a multiple of 4, write Fire instead of the number
    // If the number is a multiple of 7, write Boom instead of the number
    // If the number is a multiple of 10, repeat it 10 times in the same line in red
    ?>
</body>

</html>