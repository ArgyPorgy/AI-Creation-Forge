const api_key = "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";

const prompt = document.querySelector('input');
const generatebutton = document.querySelector('button');
const imagesection = document.querySelector('.generated-images');

async function generateimg(){



    const response = await fetch("https://api.openai.com/v1/images/generations",{
        method: "POST", headers : {
            "Content-Type": "application/json",
            "Authorization": `Bearer ${api_key}`,
        },
        body: JSON.stringify({
            prompt: prompt.value,
            n: 4,
            size : '1024x1024'
          })
});

const data = await response.json();
console.log(data);

data?.data.forEach(imageObject => {
    const imgcontainer = document.createElement('div');
    imgcontainer.classList.add('generated-images');
    const imgelement = document.createElement('img');
    imgelement.setAttribute('src',imageObject.url);
    imgcontainer.append(imgelement);
    imagesection.append(imgcontainer);
    
});

}