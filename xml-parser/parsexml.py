import xml.etree.ElementTree as Et
import glob


def parsexml(xmldirs):
    for xmldir in findfiles(xmldirs):
        tag = xmldir.split('\\')[1]

        file = open(f'../data/{tag}.txt', 'w+', encoding='utf-8')
        for xmlfile in findfiles(xmldir + '/*.xml'):
            xml = Et.parse(xmlfile)
            root = xml.getroot()


        file.close()


def findfiles(xmlfiles):
    return glob.glob(xmlfiles)


def get_abs_path(context, path=None, pathstring=''):
    if path is None:
        path = [context.tag]

    for child in context:
        text = child.text.strip() if child.text else None
        new_path = path[:]
        new_path.append(child.tag)
        if text:
            pathstring += '/'.join(new_path) + ','  # + text.replace('\n', '') + ','

        get_abs_path(child, new_path, pathstring)

    return pathstring
