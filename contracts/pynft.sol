// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/utils/Counters.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract PYNFT is ERC721, Ownable {
    uint256 public tokenCounter = 0;
    string private _baseURIextended;

    constructor() public ERC721("MyFirstPythonCode", "PYNFT") {}

    function createCollectable()
        public
        onlyOwner
        returns (uint256)
    {
        // Assign TokenId to the new owner
        // _safeMint funcation protect NFT replacement
        uint256 newTokenId = tokenCounter;
        _safeMint(
            msg.sender, // Address of who calls this function
            newTokenId // Token 0, 1, 2, ....
        );
        tokenCounter++;
        return newTokenId;
    }

    function setBaseURI(string memory baseURI_) external onlyOwner {
        _baseURIextended = baseURI_;
    }

    function _baseURI() internal view virtual override returns (string memory) {
        return _baseURIextended;
    }

    function tokenURI(uint256 tokenId)
        public
        view
        virtual
        override
        returns (string memory)
    {
        return _baseURI();
    }
}
