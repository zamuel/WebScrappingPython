import img_exctractor as i_e

if __name__ == '__main__':
    target_url = 'http://www.apress.com/'
    apress = i_e.download_page(target_url)
    image_locations = i_e.extract_imagen(apress)
    for src in image_locations:
        print(i_e.urljoin(target_url, src))