CREATE TABLE `profiles` (
    `id` BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `created_at` DATETIME NOT NULL,
    `updated_at` DATETIME NOT NULL,
    `img_url` VARCHAR(400) NOT NULL,
    `name` VARCHAR(50) NOT NULL,
    `email` VARCHAR(100) NOT NULL,
    `tel` VARCHAR(20) NOT NULL,
    `rank` VARCHAR(100) NOT NULL,
    `address` VARCHAR(500) DEFAULT NULL,
    `birthday` DATE DEFAULT NULL,
    `web_site` VARCHAR(400) NOT NULL
);

CREATE TABLE `labels` (
    `id` BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `created_at` DATETIME NOT NULL,
    `updated_at` DATETIME NOT NULL,
    `name` VARCHAR(50) NOT NULL,
    `profile_id` BIGINT NOT NULL,
    FOREIGN KEY (`profile_id`) REFERENCES `profiles` (`id`) ON DELETE CASCADE
);
