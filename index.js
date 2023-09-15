const api_key = "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";

const prompt = document.querySelector('input');
const generatebutton = document.querySelector('button');
const imagesection = document.querySelector('.generated-images');

async function generateimg(){


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