const repos= document.getElementById("getRepo")
repos.addEventListener("click", gRep)
async function gRep() {
    const url="https://api.github.com/search/repositories?q=stars:>300000"
    const response= await fetch(url)
    const divRes=document.getElementById("divRes")
    const result=await response.json()
    console.log(result)
    result.items.forEach(i=>{
        const anchor=document.createElement("a")
        anchor.href=i.html_url
        anchor.textContent=i.full_name
        divRes.appendChild(anchor)
        divRes.appendChild(document.createElement("br"))}

    )

}