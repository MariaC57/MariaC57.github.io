function addList(){
	var Activity= document.getElementById("Input").value;
 
 	var newdivs= document.createElement('div'); 

 	newdivs.innerHTML = Activity;

 	store.appendChild(newdivs);

 	var input = document.createElement('input');

 	input.type= 'checkbox';

 	newdivs.appendChild(input);

 	newdivs.className= "item"

 	input.className= "response"
 }

 	function DELETE(){
    
    var Lists = document.getElementsByClassName("item");
    var Box = document.getElementsByClassName("response");

    for (var i = 0; i < Box.length; i++) {
    	var idea = Box[i];
    	var idea2 = Lists[i];
    	if (idea.checked){
    		idea.remove();
    		idea2.remove();
    		i--
    	}
    }
 	}