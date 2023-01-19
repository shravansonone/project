
CREATE DATABASE flaskapp;
USE flaskapp;

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL
);

INSERT INTO `users` (`id`, `name`, `email`) VALUES
(2, 'Parwiz', 'parwiz.f@gmail.com');

ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);

ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;
