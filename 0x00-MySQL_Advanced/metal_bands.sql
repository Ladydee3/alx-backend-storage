CREATE TABLE metal_bands (
    id INT AUTO_INCREMENT PRIMARY KEY,
    band_name VARCHAR(255),
    formed INT,
    style VARCHAR(255)
);

INSERT INTO metal_bands (band_name, formed, style) VALUES
('Alice Cooper', 1964, 'Glam rock'),
('Mötley Crüe', 1981, 'Glam rock'),
('Marilyn Manson', 1993, 'Industrial rock'),
('The 69 Eyes', 1989, 'Gothic rock'),
('Hardcore Superstar', 1997, 'Glam rock'),
('Nasty Idols', 1987, 'Glam rock'),
('Hanoi Rocks', 1980, 'Glam rock');

