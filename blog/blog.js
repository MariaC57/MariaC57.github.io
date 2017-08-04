class BlogEntry {
	constructor(name,blogText){
//name, blogText
	this.authorName= name;
	this.blogText= blogText
}
}

function addEntryToBlog() {
	var authorName = document.getElementById("blogEntryName").value;
	var blogText = document.getElementById("blogEntryText").value;
  var blogEntry = new BlogEntry( authorName, blogText);

  //Add the new entry, name and date to the blog
  createBlogEntryElement(blogEntry);
  createFooterElement(blogEntry);

  //Clear the inputs

}

function createBlogEntryElement(blogEntry) {
 //var blogText= document.getElementById("blogEntryName")
 var blogEntryDiv= document.createElement("div");
 blogEntryDiv.className="blogEntry";
 blogEntryDiv.innerText= blogEntry.blogText;
 // var node= document.createElement("div");
 // var blogEntry= BlogEntry.blogText
  //node.innerText=""
  var blogDetails= document.getElementById("blogDetails");
  blogDetails.appendChild(blogEntryDiv);
}

function createFooterElement(blogEntry) {
  var blogFooter= document.createElement("div");
  blogFooter.className= "blogDate"
  blogFooter.innerText="by"+ blogEntry.authorName + "on" + Date();
  //var blogDetails= document.getElementById("blogEntryText")
  //var node= document.createElement("div");
  //node.innerText=""
var blogDetails = document.getElementById("blogDetails")
 blogDetails.appendChild(blogFooter);
}
