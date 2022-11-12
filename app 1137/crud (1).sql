-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 12, 2022 at 01:53 PM
-- Server version: 10.4.22-MariaDB
-- PHP Version: 8.1.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `crud`
--

-- --------------------------------------------------------

--
-- Table structure for table `clienttable`
--

CREATE TABLE `clienttable` (
  `ID` int(11) NOT NULL,
  `name` text NOT NULL,
  `email` text NOT NULL,
  `phone` text NOT NULL,
  `project` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `clienttable`
--

INSERT INTO `clienttable` (`ID`, `name`, `email`, `phone`, `project`) VALUES
(7, 'sdfsf', 'sdfasdf', 'sdfsdf', 'sdfsdf'),
(8, 'sdfsdf', 'sdfsdfdfsad', 'sdfsdf', 'sdfasdf'),
(9, 'test', 'test', 'test', 'test'),
(10, 'newclient', 'virkam mhaske', 'vikram', 'vikram'),
(11, 'vikrm', 'vikrammhaske98@gmailc.om', '09878989898', 'amv'),
(12, 'test', 'test', 'test', 'test');

-- --------------------------------------------------------

--
-- Table structure for table `students`
--

CREATE TABLE `students` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `phone` varchar(255) NOT NULL,
  `status` text NOT NULL,
  `priority` text NOT NULL,
  `d` text NOT NULL,
  `cid` int(11) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `students`
--

INSERT INTO `students` (`id`, `name`, `email`, `phone`, `status`, `priority`, `d`, `cid`) VALUES
(34, 'client 1', '621', 'd', 'in que', 'L', '2022-11-26', 0),
(28, 'three', '3', 'c', 'COMPLETED', 'H', '2022-11-03', 0),
(30, 'one', 'asd@dsf', 'vikram', 'COMPLETED', 'H', '2022-11-12', 0),
(29, 'one', 'asd@dsf', 'vikram', 'in que', 'H', '2022-11-23', 0),
(25, 'two three', 'make logo', 'muzamil', 'COMPLETED', 'H', '2022-11-11', 0),
(22, 'samsung', 'make new phone', 'c', 'COMPLETED', 'M', '2022-11-11', 0),
(32, 'two', 'vikrammhaske98@gmailc.om', 'e', 'in que', 'M', '2022-11-14', 0),
(33, 'client 1', 'asd@dsf', 'c', 'in que', 'M', '2022-11-26', 0);

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `id` int(11) NOT NULL,
  `username` text NOT NULL,
  `password` text NOT NULL,
  `role` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`id`, `username`, `password`, `role`) VALUES
(1, 'admin', 'admin', 'admin'),
(2, 'admin', 'admin', 'andwemedia'),
(3, 'admin', 'admin', 'viw3d'),
(4, 'admin', 'admin', 'micrografix');

-- --------------------------------------------------------

--
-- Table structure for table `viw3d`
--

CREATE TABLE `viw3d` (
  `id` int(11) NOT NULL,
  `name` text NOT NULL,
  `task` text NOT NULL,
  `assign` text NOT NULL,
  `status` text NOT NULL,
  `priority` text NOT NULL,
  `date_v` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `viw3d`
--

INSERT INTO `viw3d` (`id`, `name`, `task`, `assign`, `status`, `priority`, `date_v`) VALUES
(1, 'vikram', 'make sideamv', 'd', 'WIP', 'M', '2022-11-18'),
(2, 'vikram', 'Make new logo logo', 'vikram', 'in que', 'H', '2022-11-19');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `clienttable`
--
ALTER TABLE `clienttable`
  ADD PRIMARY KEY (`ID`);

--
-- Indexes for table `students`
--
ALTER TABLE `students`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `viw3d`
--
ALTER TABLE `viw3d`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `clienttable`
--
ALTER TABLE `clienttable`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `students`
--
ALTER TABLE `students`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=35;

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `viw3d`
--
ALTER TABLE `viw3d`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
