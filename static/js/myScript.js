

// Jquery functions
$(document).ready(function(){
	$('#showFilesButton').click(function(){
		$("#fileManagerDiv").load("/home/showDirAjax"+"");
	});
});



function goBack(parentPath){
	if(parentPath != '')
	$("#fileManagerDiv").load("/home/goBack/"+parentPath)
}

function deleteFolder(folderName) {
	$("#fileManagerDiv").load("/home/deleteFolder/"+folderName);

}

function showDirAjax(path){
	$("#fileManagerDiv").load('/home/showDirAjax/'+path);
}
