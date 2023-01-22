// import 'links.js'

const getSaga = link => {
    // https://multimedia.xarxacatala.cat/one-piece/saga-{saga}/op_cat-{cap_3nums}.mp4

    const saga = link.split('/')
        .filter(part => part.startsWith('saga-'))
        [0]
        .replace('saga-', '')

    return parseInt(saga)
}

const getCap = link => {
    // https://multimedia.xarxacatala.cat/one-piece/saga-{saga}/op_cat-{cap_3nums}.mp4

    const cap = link.split('/')
        .filter(part => part.startsWith('op_cat-'))
        [0]
        .replace('op_cat-', '')
        .replace('.mp4', '')

    return parseInt(cap)
}

let linksDict = {}
const sagues = [...new Set(links.map(link => getSaga(link)))]
sagues.forEach(saga => linksDict[saga] = [])

links
    .map(link => [getSaga(link), getCap(link)])
    .forEach(([saga, cap]) => linksDict[saga].push(cap))