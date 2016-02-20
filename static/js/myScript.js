// Jquery functions
$(document).ready(function(){

	$("#newFolderID").hover(function() {
		$("#newFolderFormID").toggle();
	});

});


function goBack(parentPath){
	$("#fileManagerDiv").load("/home/goBack/"+parentPath)
}

function deleteFolder(folderName) {
	$("#fileManagerDiv").load("/home/deleteFolder/"+folderName);

}

function showDirAjax(path){
	$("#fileManagerDiv").load('/home/showDirAjax/'+path);
}
