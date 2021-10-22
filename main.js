const repos= document.getElementById("getRepo")
repos.addEventListener("click", gRep)
async function gRep() {
    const url="https://api.github.com/search/repositories?q=stars:>10"
    const response= await fetch(url)
    console.log(response.json())
}