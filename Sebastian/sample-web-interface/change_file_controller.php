<?php
if (!isset($_GET["sb_target_url"])){
	echo "Please send sb_target_url GET attribute. Aborting,";
	exit(0);
}

$target = $_GET["sb_target_url"];

$filetowrite = fopen("./site-file.txt", "w") or die("Unable to open file!");
fwrite($filetowrite, "site:".$target);
fclose($filetowrite);

header("Location: ./index.html");

?>