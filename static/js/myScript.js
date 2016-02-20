// Jquery functions
$(document).ready(function(){

	$("#newFolderID").hover(function() {
		$("#newFolderFormID").toggle();
	});

});


function goBack(){
	window.history.back();
}

function deleteFolder(folderName) {
	alert(folderName);
	$("#fileManagerDiv").load("/home/deleteFolder/"+folderName);

}
